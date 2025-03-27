-- init_database.sql
CREATE TABLE IF NOT EXISTS vehicle_data (
    clip_name TEXT,
    frame_id INTEGER,
    vehicle_type TEXT,
    detection BOOLEAN,
    distance INTEGER
);
-- Optional: Add an example insert or load command
INSERT INTO vehicle_data SELECT * FROM read_parquet('/db/*.parquet');
