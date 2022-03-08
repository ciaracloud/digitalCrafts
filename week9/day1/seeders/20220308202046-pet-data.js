"use strict";

module.exports = {
  async up(queryInterface, Sequelize) {
    return await queryInterface.bulkInsert("pets", [
      {
        type: "tuxedo",
        species: "cat",
        name: "Kiwi",
        age: 2,
        ownerId: 1,
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        type: "hairless",
        species: "cat",
        name: "Baldy",
        age: 5,
        ownerId: 2,
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        type: "persian",
        species: "cat",
        name: "Princess",
        age: 4,
        ownerId: 3,
        createdAt: new Date(),
        updatedAt: new Date(),
      },
      {
        type: "siamese",
        species: "cat",
        name: "Mango",
        age: 6,
        ownerId: 4,
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
