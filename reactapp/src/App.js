import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

//import loginComponent from './logincomponent';
import HeaderComponent from './toggle';
import CollegeList from './collegelist';

import InputEx from './input';

import StudentList from './studentList';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";


class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to Bujji's World</h1>
        </header>
        <p className="App-intro">
          Hello Bujji
        </p>
        <InputEx />
        <loginComponent logged_in = {1} title = "Welcome To MRND"/>
       <HeaderComponent isLoggedIn={true} title = "Welcome To MRND"/>

        <React.Fragment>
            <Router>
                <div>
                    <Route exact path="/" render={(props) => <CollegeList  username="harithabujji" password="haritha123"/> }/>
                    <Route exact path="/college/:id/" component = {StudentList}/>

                </div>
            </Router>
        </React.Fragment>
      </div>
    );
  }

}

export default App;


