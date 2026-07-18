Parse the Apache-style access log located at `/app/access.log` and create a JSON summary report at `/app/report.json`.

Success criteria:

1. Create `/app/report.json` containing valid JSON.
2. Include `total_requests`, an integer equal to the number of non-empty log entries.
3. Include `unique_ips`, an integer equal to the number of distinct client IP addresses in the log.
4. Include `top_path`, a string containing the most frequently requested request path.
