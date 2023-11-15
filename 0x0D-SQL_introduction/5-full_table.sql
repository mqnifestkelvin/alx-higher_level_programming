-- Shows full table info
-- show create table
SELECT 
    TABLE_SCHEMA as 'Database',
    TABLE_NAME as 'Table',
    COLUMN_NAME as 'Column',
    ORDINAL_POSITION as 'Position',
    COLUMN_DEFAULT as 'Default',
    IS_NULLABLE as 'Nullable',
    DATA_TYPE as 'Data Type',
    CHARACTER_MAXIMUM_LENGTH as 'Max Length',
    COLUMN_TYPE as 'Column Type',
    COLUMN_KEY as 'Key',
    EXTRA as 'Extra',
    PRIVILEGES as 'Privileges',
    COLUMN_COMMENT as 'Comment'
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_SCHEMA = 'hbtn_0c_0' AND 
    TABLE_NAME = 'first_table';