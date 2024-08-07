CREATE SCHEMA "oqs";

CREATE TABLE "oqs"."User" (
  "user_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "email" varchar UNIQUE
);

CREATE TABLE "oqs"."Profile" (
  "profile_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "first_name" varchar,
  "middle_name" varchar,
  "last_name" varchar,
  "user_name" varchar UNIQUE,
  "date_of_birth" date,
  "role" varchar,
  "user_actions" integer
);

CREATE TABLE "oqs"."Actions" (
  "action_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "action" varchar,
  "profile_id" integer
);

CREATE TABLE "oqs"."Question" (
  "question_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "question_text" varchar,
  "question_image" image,
  "tags" integer,
  "solution_explanation" text
);

CREATE TABLE "oqs"."Option" (
  "option_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "option_text" varchar,
  "option_image" image,
  "correct_option" boolean
);

CREATE TABLE "oqs"."Solution_Explanation_Image" (
  "id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "question_id" integer,
  "image_name" varchar
);

CREATE TABLE "oqs"."Question_Set" (
  "question_set_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "question_set_name" varchar,
  "questions" integer,
  "created_by" integer,
  "answered_by" integer,
  "time_alloted" time
);

CREATE TABLE "oqs"."Tags" (
  "tag_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "tag_name" varchar,
  "questions" integer
);

CREATE TABLE "oqs"."Progress_Report" (
  "report_id" INTEGER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
  "user_id" integer,
  "question_set_id" integer,
  "generation_date" date,
  "score" integer,
  "total_score" integer
);

COMMENT ON COLUMN "oqs"."Profile"."role" IS 'ADMIN, TEACHER, STUDENT, GUEST';

COMMENT ON COLUMN "oqs"."Actions"."action" IS 'READ_QUESTION, FRAME_QUESTION, ANSWER_QUESTION';

COMMENT ON COLUMN "oqs"."Option"."correct_option" IS 'True or False';

ALTER TABLE "oqs"."Profile" ADD FOREIGN KEY ("profile_id") REFERENCES "oqs"."User" ("user_id");

CREATE TABLE "oqs"."Profile_Actions" (
  "Profile_profile_id" integer,
  "Actions_action_id" integer,
  PRIMARY KEY ("Profile_profile_id", "Actions_action_id")
);

ALTER TABLE "oqs"."Profile_Actions" ADD FOREIGN KEY ("Profile_profile_id") REFERENCES "oqs"."Profile" ("profile_id");

ALTER TABLE "oqs"."Profile_Actions" ADD FOREIGN KEY ("Actions_action_id") REFERENCES "oqs"."Actions" ("action_id");


ALTER TABLE "oqs"."Solution_Explanation_Image" ADD FOREIGN KEY ("id") REFERENCES "oqs"."Question" ("question_id");

ALTER TABLE "oqs"."Option" ADD FOREIGN KEY ("option_id") REFERENCES "oqs"."Question" ("question_id");

CREATE TABLE "oqs"."Question_Tags" (
  "Question_question_id" integer,
  "Tags_tag_id" integer,
  PRIMARY KEY ("Question_question_id", "Tags_tag_id")
);

ALTER TABLE "oqs"."Question_Tags" ADD FOREIGN KEY ("Question_question_id") REFERENCES "oqs"."Question" ("question_id");

ALTER TABLE "oqs"."Question_Tags" ADD FOREIGN KEY ("Tags_tag_id") REFERENCES "oqs"."Tags" ("tag_id");


CREATE TABLE "oqs"."Question_Question_Set" (
  "Question_question_id" integer,
  "Question_Set_question_set_id" integer,
  PRIMARY KEY ("Question_question_id", "Question_Set_question_set_id")
);

ALTER TABLE "oqs"."Question_Question_Set" ADD FOREIGN KEY ("Question_question_id") REFERENCES "oqs"."Question" ("question_id");

ALTER TABLE "oqs"."Question_Question_Set" ADD FOREIGN KEY ("Question_Set_question_set_id") REFERENCES "oqs"."Question_Set" ("question_set_id");


ALTER TABLE "oqs"."Progress_Report" ADD FOREIGN KEY ("report_id") REFERENCES "oqs"."User" ("user_id");

ALTER TABLE "oqs"."Progress_Report" ADD FOREIGN KEY ("report_id") REFERENCES "oqs"."Question_Set" ("question_set_id");
