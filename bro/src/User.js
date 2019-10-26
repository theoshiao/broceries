import React from 'react';
import {Col, Row} from 'react-bootstrap';

const User = (props) => {
  return (<div>
    <Col>
        {/**<button onClick={() => props.removeUser(props.id)}>✖</button>**/}
        { props.name }
    </Col></div>
  );
}

export default User;
