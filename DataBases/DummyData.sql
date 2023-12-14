-- Create Users
INSERT INTO Users (Name, Password, Employee) VALUES ('Geralt', 'hesterbest', 0);
INSERT INTO Users (Name, Password, Employee) VALUES ('Yennefer', 'qwerty', 0);
INSERT INTO Users (Name, Password, Employee) VALUES ('Roach', 'pizza', 0);
INSERT INTO Users (Name, Password, Employee) VALUES ('Jaskier', 'nyttpassord', 1);

-- Create Burgers
INSERT INTO Burgers (Name, Ingredients) VALUES ('Whopper Queen', 'Burgerbrød, burgerkjøtt, salat, tomat');
INSERT INTO Burgers (Name, Ingredients) VALUES ('Triple Cheesy Princess', 'Burgerbrød, burgerkjøtt, ost, salat, tomat');
INSERT INTO Burgers (Name, Ingredients) VALUES ('Kingdom Fries', 'Potet');

-- Create Orders
INSERT INTO Orders (CustomerID, BurgerID, Produced) VALUES (1, 1, 1);
INSERT INTO Orders (CustomerID, BurgerID, Produced) VALUES (1, 1, 0);
INSERT INTO Orders (CustomerID, BurgerID, Produced) VALUES (4, 2, 0);
INSERT INTO Orders (CustomerID, BurgerID, Produced) VALUES (3, 1, 0);

-- Create Ingredients
INSERT INTO Ingredients (Ingredient, Quantity) VALUES ('Burgerbrød topp og bunn', 9001);
INSERT INTO Ingredients (Ingredient, Quantity) VALUES ('Burgerkjøtt', 10);
INSERT INTO Ingredients (Ingredient, Quantity) VALUES ('Salat', 8008);
INSERT INTO Ingredients (Ingredient, Quantity) VALUES ('Tomat', 1337);
INSERT INTO Ingredients (Ingredient, Quantity) VALUES ('Ost', 42);
INSERT INTO Ingredients (Ingredient, Quantity) VALUES ('Agurk', 666);
INSERT INTO Ingredients (Ingredient, Quantity) VALUES ('Potet', 420);
