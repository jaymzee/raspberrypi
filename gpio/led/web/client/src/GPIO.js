import React from 'react';
import Button from 'react-bootstrap/Button';

class LED extends React.Component {
  state = {
    isOn: false,
  };

  handleClick = () => {
    const request = {
      method: 'PUT',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({active: !this.state.isOn})
    };
    fetch(this.props.url, request)
      .then(response => response.status === 200 ?
              response.json() :
              Promise.reject("http error " + response.status))
      .then(result => this.setState({ isOn: result.active }))
      .catch(error => console.log("cannot reach server: " + error));
  }

  render() {
    return (
      <Button onClick={this.handleClick}>
        {this.state.isOn?`${this.props.name} is on`:`${this.props.name} is off`}
      </Button>
    );
  }
}

export default LED;
