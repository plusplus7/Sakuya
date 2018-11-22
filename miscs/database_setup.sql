CREATE TABLE Users (
    id UUID DEFAULT uuid_generate_v4(),
    display_name VARCHAR NOT NULL,
    register_time TIMESTAMP NOT NULL,
    others VARCHAR
);

CREATE TABLE ExpenseRecords (
    id UUID DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    from_account UUID NOT NULL,
    to_account UUID NOT NULL,
    amount DOUBLE PRECISION NOT NULL,
    transaction_time TIMESTAMP NOT NULL,
    created_time TIMESTAMP NOT NULL,
    description VARCHAR
);

CREATE TABLE Accounts (
    id UUID DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL,
    display_name VARCHAR NOT NULL,
    balance DOUBLE PRECISION NOT NULL
);