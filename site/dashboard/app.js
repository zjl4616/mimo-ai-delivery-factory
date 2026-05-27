const statusClasses = {
  healthy: "is-healthy",
  late: "is-late",
  stale: "is-stale",
  unknown: "is-unknown",
};

function setText(id, value) {
  document.getElementById(id).textContent = value;
}

function formatTime(value) {
  if (!value) return "暂无记录";
  return new Intl.DateTimeFormat("zh-CN", {
    month: "2-digit",
    day: "2-digit",
    hour: "2-digit",
    minute: "2-digit",
  }).format(new Date(value));
}

function statusTag(product) {
  const label = product.stage || product.status;
  const klass = product.status === "online" ? "is-healthy" : product.status === "building" ? "is-late" : "is-unknown";
  return `<span class="tag ${klass}">${label}</span>`;
}

function renderProducts(products) {
  const list = document.getElementById("productList");
  list.innerHTML = products
    .map(
      (product) => `
        <article class="product-item">
          <div class="product-id">${product.id}</div>
          <div class="product-main">
            <div class="product-title">
              <strong>${product.name}</strong>
              ${statusTag(product)}
            </div>
            <p>${product.channel}</p>
            <p>${product.next}</p>
            ${product.url ? `<p><a href="${product.url}">打开公开页面</a></p>` : ""}
            <div class="progress" aria-label="${product.name} 进度 ${product.progress}%">
              <span style="width: ${product.progress}%"></span>
            </div>
          </div>
        </article>
      `,
    )
    .join("");
}

function renderRuns(runs) {
  const list = document.getElementById("runList");
  if (!runs.length) {
    list.innerHTML = '<article class="run-item"><strong>暂无服务器产出</strong><p>等待下一轮后台运行。</p></article>';
    return;
  }
  list.innerHTML = runs
    .map(
      (run) => `
        <article class="run-item">
          <header>
            <strong>${run.title}</strong>
            <span class="run-file">${run.file}</span>
          </header>
          <p>${run.choice || "本轮选择未提取。"}</p>
          <p>更新时间：${formatTime(run.updatedAt)}</p>
        </article>
      `,
    )
    .join("");
}

function renderPromotion(promotion) {
  setText("promotionLabel", promotion.label);
  setText("promotionNext", promotion.nextAction);
  document.getElementById("channelList").innerHTML = promotion.nextChannels.map((channel) => `<span>${channel}</span>`).join("");
}

function renderConfirmation(items) {
  const list = document.getElementById("confirmationList");
  list.innerHTML = items
    .map(
      (item) => `
        <article class="confirmation-item">
          <strong>${item.type}</strong>
          <p>${item.text}</p>
        </article>
      `,
    )
    .join("");
}

function render(data) {
  const health = data.health || { status: "unknown", label: "未知" };
  const pill = document.getElementById("healthPill");
  pill.className = `health-pill ${statusClasses[health.status] || "is-unknown"}`;
  pill.textContent = health.status;

  setText("healthLabel", health.label);
  setText(
    "healthMeta",
    `最近运行：${formatTime(health.latestRunAt)}；距离现在 ${health.latestRunAgeMinutes ?? "--"} 分钟；计划：每 30 分钟。`,
  );
  setText("productsTotal", data.metrics.productsTotal);
  setText("productsOnline", data.metrics.productsOnline);
  setText("serverRuns", data.metrics.serverRuns);
  setText("revenueState", data.metrics.revenueState.replace("暂无", "0 "));
  setText("generatedAt", `快照：${formatTime(data.generatedAt)}`);
  setText("safetyNote", data.safety.note);

  renderProducts(data.products || []);
  renderPromotion(data.promotion || { label: "--", nextAction: "--", nextChannels: [] });
  renderRuns(data.recentRuns || []);
  renderConfirmation(data.confirmationQueue || []);
}

async function loadStatus() {
  try {
    const response = await fetch("./status.json", { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    render(await response.json());
  } catch (error) {
    document.getElementById("healthPill").className = "health-pill is-stale";
    setText("healthPill", "error");
    setText("healthLabel", "状态快照读取失败");
    setText("healthMeta", String(error));
  }
}

loadStatus();
setInterval(loadStatus, 60_000);
