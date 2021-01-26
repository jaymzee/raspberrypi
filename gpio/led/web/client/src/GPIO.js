import React from 'react';
import Button from 'react-bootstrap/Button';

class GPIO extends React.Component {
  state = {
    isOn: false,
  };

  handleClick = async () => {
    const request = {
      method: 'PUT',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({active: !this.state.isOn})
    };
    try {
      const response = await fetch(this.props.url, request);
      if (response.status !== 200) {
        throw new Error("http error: " + response.status);
      }
      const json = await response.json();
      this.setState({isOn: json.active});
    } catch (error) {
      console.log("cannot reach server: " + error);
    }
  }

  render() {
    return (
      <Button onClick={this.handleClick}>
        {this.state.isOn ?
          `${this.props.name} is on` :
          `${this.props.name} is off`}
      </Button>
    );
  }
}

export default GPIO;
