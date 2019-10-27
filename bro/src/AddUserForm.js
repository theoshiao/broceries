import React, {Component} from 'react';

class AddUserForm extends Component {
  state = {
    value: ''
  };

  handleValueChange = (e) => {
    this.setState({value: e.target.value});
  }

  handleSubmit = (e) => {
    e.preventDefault();
    this.props.addUser(this.state.value);
    this.state.value = '';

  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <input
          type="text"
          value={this.state.value}
          onChange={this.handleValueChange}
          placeholder="Enter a name"
          />
        <input
          type="submit"
          value="Add User"
          />
      </form>
    );
  }
}

export default AddUserForm;
