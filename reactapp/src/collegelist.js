import React, { Component } from 'react';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";
import StudentList from './studentList'

class CollegeList extends Component {

    state ={
        collegesList : []
    }
    componentDidMount(){

        const hash = Buffer.from(`${this.props.username}:${this.props.password}`).toString('base64');

        fetch('http://127.0.0.1:8000/onlineapp/clg/',
             {
                      method: 'get',
           headers: new Headers({
             'Authorization': `Basic ${hash}`,
             'Content-Type': 'application/x-www-form-urlencoded',
           }),
         })
          .then(response => response.json())
        .then(responseJson => {
        this.setState({ collegesList : responseJson});
        })
        .catch(e => {console.log ("Error");});
    }


    render(){
    return(
        <React.Fragment>
            <div className="container">
                <table className="table table-bordered">
                    <thead>
                        <th>Acronym</th>
                        <th>College Name</th>
                        <th>Location</th>
                        <th>Contact</th>
                    </thead>
                    <tbody>
                    {this.state.collegesList.map(item => (
                        <tr key={item.id}>
                            <td>{item.name}</td>
                            <td><Link to={'/college/' + item.id}>{item.acronym}</Link></td>
                            <td>{item.location}</td>
                            <td>{item.contact}</td>
                        </tr>

                    ))}
                    </tbody>

                </table>
            </div>
        </React.Fragment>
        );
    }
}

export default CollegeList




