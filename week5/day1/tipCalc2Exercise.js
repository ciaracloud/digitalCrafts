function totalAmount(bill, service) {
  service = service.toLowerCase();
  if (service === "good") {
    tip = bill * 0.2;
    bill = tip + bill;
    console.log(bill);
  } else if (service === "fair") {
    tip = bill * 0.15;
    bill = tip + bill;
    console.log(bill);
  } else if (service == "bad") {
    tip = bill * 0.1;
    bill = tip + bill;
    console.log(bill);
  }
}
