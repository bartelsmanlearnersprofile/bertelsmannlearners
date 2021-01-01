BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `learners` (
    `id` INTEGER NOT NULL,
    `slackname` VARCHAR(200) NOT NULL,
    `firstname` VARCHAR(200) NOT NULL,
    `lastname` VARCHAR(200) NOT NULL,
    PRIMARY KEY(`id`)
);

INSERT INTO `learners` (slackname, firstname, lastname) VALUES ('udoyen', 'George', 'Udosen'),
    ('nicce', 'Kenneth', 'Udosen'), ('udoyen1', 'Koo', 'Udosen'), ('mowa', 'David', 'Ekanem' ),
    ('m2', 'David', 'Ekanem' );
COMMIT;