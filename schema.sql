DROP TABLE IF EXISTS prompts;

CREATE TABLE prompts (
  Created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  Activity TEXT NOT NULL,
  Subclass TEXT NOT NULL,
  Primaryweapon TEXT NOT NULL, 
  PrimaryPerks TEXT NOT NULL,
  Secondaryweapon TEXT NOT NULL,
  SecondaryPerks TEXT NOT NULL,
  Heavyweapon TEXT NOT NULL,
  HeavyPerks TEXT NOT NULL
);

