CREATE TABLE "User" (
	"mail" TEXT NOT NULL,
	"password" TEXT,
	"firstName" TEXT,
	"lastName" TEXT,
	PRIMARY KEY("mail")
);
CREATE TABLE "Post" (
	"postID" INTEGER NOT NULL,
	"mail" TEXT,
	"coffeeID" INTEGER,
	"note" TEXT,
	"score" INTEGER,
	"date" TEXT,
	FOREIGN KEY("coffeeID") REFERENCES "Coffee"("coffeeID") ON UPDATE CASCADE ON DELETE NO ACTION,
	FOREIGN KEY("mail") REFERENCES "User"("mail") ON UPDATE CASCADE ON DELETE NO ACTION,
	PRIMARY KEY("postID" AUTOINCREMENT)
);
CREATE TABLE "Coffee" (
	"coffeeID" INTEGER NOT NULL,
	"roasteryID" INTEGER,
	"batchID" INTEGER,
	"date" TEXT,
	"coffeeName" TEXT,
	"description" TEXT,
	"priceKG" NUMERIC,
	"roastGrade" INTEGER,
	FOREIGN KEY("batchID") REFERENCES "Batch"("batchID") ON UPDATE CASCADE ON DELETE NO ACTION,
	FOREIGN KEY("roasteryID") REFERENCES "CoffeeRoastery"("roasteryID") ON UPDATE CASCADE ON DELETE NO ACTION,
	PRIMARY KEY("coffeeID")
);
CREATE TABLE "CoffeeRoastery" (
	"roasteryID" INTEGER NOT NULL,
	"name" TEXT,
	PRIMARY KEY("roasteryID" AUTOINCREMENT)
);
CREATE TABLE "Batch" (
	"batchID" INTEGER NOT NULL,
	"methodID" INTEGER,
	"farmID" INTEGER,
	"harvestYear" INTEGER,
	"price" NUMERIC,
	FOREIGN KEY("methodID") REFERENCES "ProcessingMethod"("methodID") ON UPDATE CASCADE ON DELETE NO ACTION,
	FOREIGN KEY("farmID") REFERENCES "Farm"("farmID") ON UPDATE CASCADE ON DELETE NO ACTION,
	PRIMARY KEY("batchID" AUTOINCREMENT)
);
CREATE TABLE "Cultivate" (
	"farmID" INTEGER,
	"typeID" INTEGER,
	FOREIGN KEY("typeID") REFERENCES "CoffeeBean"("typeID") ON UPDATE CASCADE ON DELETE NO ACTION,
	FOREIGN KEY("farmID") REFERENCES "Farm"("farmID") ON UPDATE CASCADE ON DELETE NO ACTION
);
CREATE TABLE "Contains" (
	"batchID" INTEGER,
	"typeID" INTEGER,
	FOREIGN KEY("batchID") REFERENCES "Batch"("batchID") ON UPDATE CASCADE ON DELETE NO ACTION,
	FOREIGN KEY("typeID") REFERENCES "CoffeeBean"("typeID") ON UPDATE CASCADE ON DELETE NO ACTION
);
CREATE TABLE "Farm" (
	"farmID" INTEGER NOT NULL,
	"name" TEXT,
	"m.a.s.l" INTEGER,
	"region" TEXT,
	"country" TEXT,
	PRIMARY KEY("farmID" AUTOINCREMENT)
);
CREATE TABLE "ProcessingMethod" (
	"methodID" INTEGER NOT NULL,
	"name" TEXT,
	"description" TEXT,
	PRIMARY KEY("methodID" AUTOINCREMENT)
);
CREATE TABLE "CoffeeBean" (
	"typeID" INTEGER NOT NULL,
	"name" TEXT,
	"species" TEXT,
	PRIMARY KEY("typeID" AUTOINCREMENT)
);