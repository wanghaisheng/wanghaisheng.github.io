---
title: "Name of Your Dish"
description: "A short description of the dish. Aim for one or two sentences that evoke taste and appeal."

author: "Your Name, GitHub Username or Alias" # Optional, if not provided, remove the block, will be set to default "anonymous".
pubDate: YYYY-MM-DD  # Publication date when you are writing the recipe.

image: ""  # Optional: URL of an image or relative path to an image within the repository.
imageAlt: ""  # Optional: A brief description of the image for accessibility.

cookingTime:  # Cooking time in minutes.

steps:
  - title: "Step Name" # Optional, can be left blank
    actions:
      - "Action to perform in this step."
      - "Another action to perform in this step."
  # Repeat the above block for each step in the recipe process.

ingredients:
  - title: "Ingredient List Title" # Example: "For the Pastry Crust:", "For the Lemon Filling:" (Optional, can be left blank if there's no separate list title)
    items:
      - quantity: "1/2" # Use fractional numbers like 1/2 or decimal numbers like 0.5.
        name: "tablespoon vegetable oil" # Include the unit of measurement followed by the ingredient, such as "tablespoon vegetable oil" or "cup water".
      - quantity: "" # If an ingredient does not require a specific quantity, such as "Salt and pepper to taste", leave the quantity blank.
        name: "Salt and pepper to taste"
      # Repeat the above item block for each ingredient in the list.

  # If the recipe has separate parts, like crust and filling, repeat the entire title and items block for each part.

recipeNotes: [
  "Any notable tips, tricks, or warnings about the recipe, separated by comma",
  # Include additional notes as list items.
] 
  # Optional, if none, remove the recipeNotes block

tags: ["tag1", "tag2", "tag3"]  # Describe the dish with appropriate tags, max 3 tags

slug: name-of-your-dish  # A URL-friendly version of your recipe's title.

---
