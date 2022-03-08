"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class owners extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      this.belongsTo(models.pets, {
        foreignKey: "ownerId",
      });
    }
  }
  owners.init(
    {
      name: DataTypes.STRING,
      password: DataTypes.STRING,
      location: DataTypes.STRING,
      enviornment: DataTypes.STRING,
    },
    {
      sequelize,
      modelName: "owners",
    }
  );
  return owners;
};
