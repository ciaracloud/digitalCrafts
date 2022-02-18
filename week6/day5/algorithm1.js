Input: (list1 = [1, 2, 4]), (list2 = [1, 3, 4]);

const mergeLists = (list1, list2) => {
  const outputList = [...list1, ...list2];
  outputList.sort();
  return outputList;
};

// Output: [1,1,2,3,4,4]
