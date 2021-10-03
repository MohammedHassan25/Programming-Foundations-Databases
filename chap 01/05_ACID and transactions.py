# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A transaction is a set of operations that must all be completed, and if for some reason any of the individual operations aren't completed, no changes are made to the database.
# Transactions follow a set of principles outlined by the acronym ACID, which requires that the transactions be atomic, consistent, isolated, and durable.
# Atomic here means that the transaction is indivisible, that pieces of it can't be separated out.
# Consistency means that whatever the transaction does, it needs to leave the database in a valid or consistent state.
# Isolation means that while the activities in the transaction are being completed, nothing else can make changes to the data involved.
# Durability means that the information we change in the transaction actually gets written to the database.
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
