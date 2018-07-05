

import React, { Component } from 'react';

class StudentList extends Component {

    state ={
        studentList : []

    }
    componentDidMount(){
      const username = "harithabujji";
      const password = "haritha123";
    const hash = Buffer.from(`${username}:${password}`).toString('base64');
    fetch('http://127.0.0.1:8000/onlineapp/clgst/' + this.props.match.params.id + '/', {
   method: 'get',
   headers: new Headers({
     'Authorization': `Basic ${hash}`,
     'Content-Type': 'application/x-www-form-urlencoded',
   }),
 })

        .then(response => response.json())
        .then(responseJson => {
        this.setState({ studentList : responseJson});
        })
        .catch(e => {console.log (e);});
    }


    render(){
    return(
        <React.Fragment>
            <div>
                <table>
                    <thead>
                        <th>Name</th>
                        <th>Db Name</th>
                        <th>Email</th>
                    </thead>
                    <tbody>
                    {this.state.studentList.map(item => (
                        <tr key={item.id}>
                            <td>{item.name}</td>
                            <td>{item.db_folder}</td>
                            <td>{item.email}</td>
                        </tr>

                    ))}
                    </tbody>

                </table>
            </div>
        </React.Fragment>
        );
    }
}

export default StudentList