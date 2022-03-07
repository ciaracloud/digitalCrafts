"use strict";
const { Model } = require("sequelize");
module.exports = (sequelize, DataTypes) => {
  class test3 extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  }
  test3.init(
    {
      color: DataTypes.STRING,
      number: DataTypes.INTEGER,
      password: DataTypes.STRING,
    },
    {
      sequelize,
      modelName: "test3",
    }
  );
  return test3;
};
