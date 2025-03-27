from dataclasses import dataclass
import typing as t

@dataclass
class QueryResult:
    """
    Represents a generic query result with typed data.
    
    Attributes:
        data: Pandas DataFrame containing query results
        metadata: Optional additional metadata about the query
    """
    data: t.Any
    metadata: t.Optional[t.Dict[str, t.Any]] = None