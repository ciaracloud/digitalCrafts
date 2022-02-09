function tipAmount(bill, service) {
  service = service.toLowerCase();
  if (service === "good") {
    tip = bill * 0.2;
    console.log(tip);
  } else if (service === "fair") {
    tip = bill * 0.15;
    console.log(tip);
  } else if (service == "bad") {
    tip = bill * 0.1;
    console.log(tip);
  }
}
