import React, {Component} from 'react';

class AddBro extends Component {
  state = {
    value: ''
  };

  handleValueChange = (e) => {
    this.setState({value: e.target.value});
  }

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.addPlayer(this.state.value);
  }

  render() {
    return (

      <form onSubmit={this.handleSubmit}>
        <input
          type="text"
          value={this.state.value}
          onChange={this.handleValueChange}
          placeholder="Enter a  name"
          />
        <input
          type="submit"
          value="Add Bro"
          />
      </form>
    );
  }
}

export default AddBro;
