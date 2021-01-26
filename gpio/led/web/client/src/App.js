import logo from './logo.svg';
import './App.css';
import GPIO from './GPIO';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <GPIO name="vacuum pump" url="/leds/green" /> &nbsp;
        <GPIO name="magnet" url="/leds/red" /> &nbsp;
        <GPIO name="laser" url="/leds/blue" /> <br />
        <GPIO name="coffee maker" url="/leds/yellow" /> <br />
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
