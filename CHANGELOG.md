# Changelog

## Iteration 1: Initial Implementation (Draft)
**What**: Built core pipeline—parse JSON, validate records, aggregate stats.
**Why**: Establishes baseline: raw_data → validated records → aggregated output.
**Status**: MVP working; no error handling, no type hints.

---

## Iteration 2: Robustness & Types (Improved)
**What**: 
- Added comprehensive error handling (JSONDecodeError, missing fields, type validation)
- Added full type hints for clarity and IDE support
- Extracted validation logic into reusable `Validator` class

**Why**: 
- Error handling prevents silent failures in production
- Type hints make intent clear and catch bugs early
- Extracted validator is now testable in isolation

**Files Changed**: `feature.py`

---

## Iteration 3: Performance Pattern (Optimized)
**What**:
- Extracted record filtering into a reusable `Filter` class
- Replaced manual validation loop with generator—reduces memory on large datasets
- Added batch processing for streaming data

**Why**:
- Generator yields records one at a time; no intermediate list
- Batch processing pattern now available for other pipelines
- Memory usage drops from O(n) to O(1) for validation

**Files Changed**: `feature.py`, introduced `validators.py` for reusable patterns

---

## Reusable Pattern Discovered
**`ValidatedPipeline` abstraction**
```python
class ValidatedPipeline:
    """Generic validator + aggregator for any record type."""
    def __init__(self, validators):
        self.validators = validators  # chain of validations
    def process(self, records):
        # yield-based filtering—zero-copy
        return self.aggregate(record for record in records 
                             if all(v.validate(record) for v in self.validators))
```

This pattern extracted during iteration 3, now reused across team for all new data pipelines.

---

## Summary
- **V1**: Working MVP (100 LOC)
- **V2**: +40 LOC, error handling, types
- **V3**: +30 LOC, zero-copy validation, reusable `ValidatedPipeline` class

**Total**: 3 ships in one day. Every improvement documented & shared.
