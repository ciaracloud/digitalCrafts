"use strict";

module.exports = {
  async up(queryInterface, Sequelize) {
    return await queryInterface.bulkInsert("owners", [
      {
        name: "Ciara",
        password: "111",
        location: "Florida",
        enviornment: "suburbs",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        name: "Jason",
        password: "222",
        location: "Illinois",
        enviornment: "suburbs",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        name: "Rayleigh",
        password: "333",
        location: "Georgia",
        enviornment: "suburbs",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        name: "Santos",
        password: "444",
        location: "Kiwi",
        enviornment: "country",
        createdAt: new Date(),
        updatedAt: new Date(),
      },
    ]);
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  },
};
