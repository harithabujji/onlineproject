//import React, { Component } from 'react';
//
//class CollegesList extends Component
//{
//
//state={
//data:null
//}
//
//componentDidMount() {
//fetch('http://127.0.0.1:8000/onlineapp/clg/')
//.then(response=>response.json())
//.then(responsejson=>{
//console.log(responsejson);
//this.setState({data:responsejson});
//})
//.catch(e=>
//{
//console.log(e)
//console.log("error occured");});
//}
//
//  render(){
//    return(
//       <h2>CollegesList</h2>
//       {
//       this.state.data && this.state.data.map(d => <p key ={d.id} > {d.name} </p> )
//       }
//       )
//    }
//}
//export default CollegesList

import React, { Component } from 'react';
class collegeList extends Component {
    state = {
        data: null,
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000/onlineapp/clg/")
            .then(Response => Response.json())
            .then(ResponseJson => this.setState({ data: ResponseJson }))
    }
    render() {

        return (
            <div>
            <h1>Colleges</h1>

                {
                    this.state.data &&
                    this.state.data.map(college =>
                        <div key = {college.id}>
                            {college.name}
                        </div>
                    )
                }
            </div>
        )
    }
}
export default CollegeList
