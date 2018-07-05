
import React from 'react';
import './App.css';

class HeaderComponent extends React.Component{
    state = {
        isLoggedIn : this.props.isLoggedIn
    }
    toggleLoggedIn = () => {
        this.setState(prev => ({isLoggedIn : !prev.isLoggedIn}))
    }
    render(){
    const {title} = this.props;
    const {isLoggedIn} = this.state;
    return(
        <div className = "App-login">

        <h2>{title}</h2>
        <div className = "menu" onClick = {this.toggleLoggedIn}>
        {
            isLoggedIn ?
            <span> <button>login </button></span>
            : <span> <button>logout </button></span>
        }
        </div>
       </div>
    )
   }
  }



export default HeaderComponent;
