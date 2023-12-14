-- Insert data into Users table
INSERT INTO Users (UserID, Name, Password, Employee) VALUES
  (1, 'Geralt', 'hesterbest', 0),
  (2, 'Yennefer', 'qwerty', 0),
  (3, 'Roach', 'pizza', 0),
  (4, 'Jaskier', 'nyttpassord', 1);

-- Insert data into Burgers table
INSERT INTO Burgers (BurgerID, Name, Ingredients) VALUES
  (1, 'Whopper Queen', 'Burgerbrød, burgerkjøtt, salat, tomat'),
  (2, 'Triple Cheesy Princess', 'Burgerbrød, burgerkjøtt, ost, salat, tomat'),
  (3, 'Kingdom Fries', 'Potet');

-- Insert data into Orders table
INSERT INTO Orders (OrderID, CustomerID, BurgerID, Produced) VALUES
  (1, 1, 1, 1),
  (2, 1, 1, 0),
  (3, 4, 2, 0),
  (4, 3, 1, 0);

-- Insert data into Ingredients table
INSERT INTO Ingredients (IngredientID, Ingredient, Quantity) VALUES
  (1, 'Burgerbrød topp og bunn', 9001),
  (2, 'Burgerkjøtt', 10),
  (3, 'Salat', 8008),
  (4, 'Tomat', 1337),
  (5, 'Ost', 42),
  (6, 'Agurk', 666),
  (7, 'Potet', 420);
