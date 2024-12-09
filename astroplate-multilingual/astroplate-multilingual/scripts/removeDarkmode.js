const fs = require("fs");
const path = require("path");

(function () {
  const rootDirs = ["src/pages", "src/hooks", "src/layouts", "src/styles"];

  const deleteAssetList = [
    "public/images/logo-darkmode.png",
    "src/layouts/components/ThemeSwitcher.astro",
  ];

  const configFiles = [
    {
      filePath: "tailwind.config.js",
      patterns: ["darkmode:\\s*{[^}]*},", 'darkMode:\\s*"class",'],
    },
    { filePath: "src/config/theme.json", patterns: ["colors.darkmode"] },
  ];

  const filePaths = [
    {
      filePath: "src/layouts/partials/Header.astro",
      patterns: [
        "<ThemeSwitchers*(?:\\s+[^>]+)?\\s*(?:\\/\\>|>([\\s\\S]*?)<\\/ThemeSwitchers*>)",
      ],
    },
  ];

  filePaths.forEach(({ filePath, patterns }) => {
    removeDarkModeFromFiles(filePath, patterns);
  });

  deleteAssetList.forEach(deleteAsset);
  function deleteAsset(asset) {
    try {
      fs.unlinkSync(asset);
      console.log(`${path.basename(asset)} deleted successfully!`);
    } catch (error) {
      console.error(`${asset} not found`);
    }
  }

  rootDirs.forEach(removeDarkModeFromPages);
  configFiles.forEach(removeDarkMode);

  function removeDarkModeFromFiles(filePath, regexPatterns) {
    const fileContent = fs.readFileSync(filePath, "utf8");
    let updatedContent = fileContent;
    regexPatterns.forEach((pattern) => {
      const regex = new RegExp(pattern, "g");
      updatedContent = updatedContent.replace(regex, "");
    });
    fs.writeFileSync(filePath, updatedContent, "utf8");
  }

  function removeDarkModeFromPages(directoryPath) {
    const files = fs.readdirSync(directoryPath);

    files.forEach((file) => {
      const filePath = path.join(directoryPath, file);
      const stats = fs.statSync(filePath);
      if (stats.isDirectory()) {
        removeDarkModeFromPages(filePath);
      } else if (stats.isFile()) {
        removeDarkModeFromFiles(filePath, [
          '(?:(?!["])\\S)*dark:(?:(?![,;"])\\S)*',
        ]);
      }
    });
  }

  function removeDarkMode(configFile) {
    const { filePath, patterns } = configFile;
    if (filePath === "tailwind.config.js") {
      removeDarkModeFromFiles(filePath, patterns);
    } else {
      const contentFile = JSON.parse(fs.readFileSync(filePath, "utf8"));
      patterns.forEach((pattern) => deleteNestedProperty(contentFile, pattern));
      fs.writeFileSync(filePath, JSON.stringify(contentFile));
    }
  }

  function deleteNestedProperty(obj, propertyPath) {
    const properties = propertyPath.split(".");
    let currentObj = obj;
    for (let i = 0; i < properties.length - 1; i++) {
      const property = properties[i];
      if (currentObj.hasOwnProperty(property)) {
        currentObj = currentObj[property];
      } else {
        return; // Property not found, no need to continue
      }
    }
    delete currentObj[properties[properties.length - 1]];
  }
})();
