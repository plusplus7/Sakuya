INSERT INTO Users(id, display_name, register_time, others)
    VALUES('00000000-0000-0000-0000-000000000001', 'Alice', current_timestamp, 'This is a test user. hahahaha');

INSERT INTO Accounts(id, user_id, display_name, balance)
    VALUES('11111111-0000-0000-0000-000000000001','00000000-0000-0000-0000-000000000001', '银行卡', 2333.33);

INSERT INTO Accounts(id, user_id, display_name, balance)
    VALUES('11111111-0000-0000-0000-000000000002','00000000-0000-0000-0000-000000000001', '支付宝', 100);

INSERT INTO Accounts(id, user_id, display_name, balance)
    VALUES('11111111-0000-0000-0000-000000000003','00000000-0000-0000-0000-000000000001', '吃喝', 0);

INSERT INTO Accounts(id, user_id, display_name, balance)
    VALUES('11111111-0000-0000-0000-000000000004','00000000-0000-0000-0000-000000000001', '娱乐', 0);

INSERT INTO expenserecords(user_id, from_account, to_account, amount, description, transaction_time, created_time)
    VALUES('00000000-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000003', 242.24, '汉堡王', current_timestamp, current_timestamp);

INSERT INTO expenserecords(user_id, from_account, to_account, amount, description, transaction_time, created_time)
    VALUES('00000000-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000004', 342.24, '买PS4', current_timestamp, current_timestamp);

INSERT INTO expenserecords(user_id, from_account, to_account, amount, description, transaction_time, created_time)
    VALUES('00000000-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000003', 442.24, '奈雪',current_timestamp, current_timestamp);

INSERT INTO expenserecords(user_id, from_account, to_account, amount, description, transaction_time, created_time)
    VALUES('00000000-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000002', '11111111-0000-0000-0000-000000000004', 42.24, 'Steam',current_timestamp, current_timestamp);

INSERT INTO expenserecords(user_id, from_account, to_account, amount, description, transaction_time, created_time)
    VALUES('00000000-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000002', '11111111-0000-0000-0000-000000000003', 2.24, '星巴克', current_timestamp, current_timestamp);

INSERT INTO expenserecords(user_id, from_account, to_account, amount, description, transaction_time, created_time)
    VALUES('00000000-0000-0000-0000-000000000001', '11111111-0000-0000-0000-000000000002', '11111111-0000-0000-0000-000000000004', 12.24, '热水冲唧唧', current_timestamp, current_timestamp);
