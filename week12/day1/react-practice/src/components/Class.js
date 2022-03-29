import React from "react";

class ClassComponent extends React.Component {
  //state - a place you can store info you want to use later on
  state = {
    counter: 0,
    word: [],
  };

  changeCount = (event) => {
    if (event.target.name === "increment") {
      this.setState({
        counter: this.state.counter + 1,
      });
    } else if (this.state.counter > 0) {
      this.setState({
        counter: this.state.counter - 1,
      });
    }
  };

  printInput = (event) => {
    const input = this.state.word.push(input);
  };

  render() {
    return (
      <div>
        <h1>Classes</h1>
        <h1>{this.state.counter}</h1>
        <button name="increment" onClick={(e) => this.changeCount(e)}>
          Increment
        </button>
        <button name="decrement" onClick={(e) => this.changeCount(e)}>
          Decrement
        </button>
        <input onChange={(e) => inputWord.e.target.value} type="text" />
        <button onClick={this.printInput}>Submit</button>
        <h1>{this.state.word}</h1>
      </div>
    );
  }
}

export default ClassComponent;
