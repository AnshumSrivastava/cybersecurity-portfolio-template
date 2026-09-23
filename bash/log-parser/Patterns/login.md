# Login Log Pattern

## Regex

```regex
^(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<action>[A-Z]+)\s+(?P<user>[a-zA-Z]+)\s+(?P<result>SUCCESS|FAILED)$
```

## Fields

| Field  | Description          |
| ------ | -------------------- |
| time   | Time of the event    |
| action | Action performed     |
| user   | Username             |
| result | Result of the action |
