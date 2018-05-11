CREATE TABLE lab.followee (
  from_id   VARCHAR(20) NOT NULL,
  follow_id VARCHAR(20) NOT NULL,
  PRIMARY KEY (from_id, follow_id)
);