# Case Study: Inquiry Reply Automation

## Scenario

A business receives repeated customer inquiries. Each reply requires reading the inquiry, matching product data, drafting a response, and sending it for review.

## Problem

Manual replies take too long and are easy to get wrong when product information is scattered.

## Prototype Workflow

1. Capture new inquiry
2. Extract product, quantity, and use case
3. Match against a product table
4. Generate a reply draft
5. Send draft to Feishu or WeChat for human review
6. Send only after approval

## Expected Result

- reduce reply drafting time
- keep human approval in the loop
- improve consistency
- expose missing product data

## Reusable Assets

- product table schema
- prompt for requirement extraction
- prompt for reply drafting
- approval checklist
- maintenance checklist

## Notes

This public case is sanitized from internal notes. It does not include private customer data, credentials, or platform-specific access details.
