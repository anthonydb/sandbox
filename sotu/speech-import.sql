
-- Import from psql

\copy sotu_speech (president, title, speech_date, speech_text) FROM 'president_speeches.csv' WITH (FORMAT CSV, DELIMITER '|', HEADER OFF, QUOTE '@');


-- Convert speeches to tsvector in the search_speech_text column

UPDATE sotu_speech SET search_speech_text = to_tsvector('english', speech_text);