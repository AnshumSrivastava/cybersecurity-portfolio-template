# Apache Log Pattern

## Regex

```regex
^\[(?P<timestamp>[^\]]+)\]\s+\[(?P<level>[^\]]+)\]\s+(?:\[client (?P<ip>[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\]\s+)?(?P<message>.*)$
```

## Fields

| Field     | Description                |
| --------- | -------------------------- |
| timestamp | Timestamp of the log event |
| level     | Log severity               |
| ip        | Client IP if present       |
| message   | Remaining log message      |
