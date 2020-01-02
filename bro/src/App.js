import React from 'react';
import User from './User.js'
import AddUserForm from './AddUserForm.js'
import ItemSelect from './ItemSelect.js'
import logo from './logo.svg';
import './App.css';
import {Col, Row, Jumbotron} from 'react-bootstrap';
// import '../node_modules/react-bootstrap'
// import Col from 'react-bootstrap/Col.js'
// import Row from 'react-bootstrap/Row.js'

class App extends React.Component {
  state = {
    users: [
    {
      name: "",
      items: [],
      id: 0
    }
  ],
    data : {
      "apple": 5.00,
      "banana": 3.99
    }
};

  handleAddUser = (name) => {
    this.setState( prevState => {
      return{
        users: [
          ...prevState.users,
          {
            name,
            items: [],
            id: this.prevPlayerId += 1
          }
        ]
    };
  });
  }

  imageUpload = () => {
    const axios = require('axios').default;
    var fileObj = this.fileUpload.files[0];
    console.log(fileObj)
    const formData = new FormData();
    formData.append("file", fileObj);
    axios.post('http://127.0.0.1:5000/uploadphoto', formData).then(function (response) {
      console.log(response.data);
      }).catch(function (error) {
        console.log(error);
      }
    );
  }

  handleRemoveUser = (id) => {
    this.setState( prevState => {
      return {
        users: prevState.users.filter(p => p.id !== id)
      };
    });
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
        <Row>
          <Col>
            <h1> BROCERIES </h1>
            <img src={logo}/>

             Split your groceries with your bros.

             <Col className="scoreboard">

               {this.state.users.map( (user, index) =>
                 <User
                     name={user.name}
                     items={user.items}
                     id={user.id}
                     index={index}
                     key={user.id.toString()}
                     removeUser={this.handleRemoveUser}
                     />

             )}
             <AddUserForm addUser={this.handleAddUser}/>

                <input type='file' label='Upload'
                  ref={(ref) => this.fileUpload = ref} name = "file" />
                <input onClick={this.imageUpload} type = "submit"/>

             </Col>

           </Col>


          </Row>
        </header>
        <ItemSelect itemList={this.state.data}
                    users = {this.state.users}/>

      </div>
    )
  }

}
export default App;
