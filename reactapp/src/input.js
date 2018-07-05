import React,{Component} from 'react'

class InputEx extends Component{

    state = {
    name : '',pass : ''
    };

    saveName=(event)=>{

        const {target :{value}} = event;
        this.setState({
            name:value
        });

    }

    savePass = (event)=>{

        const {target :{value}} = event;
        this.setState({
            pass:value
        });
    }

    submit = (e) =>{
   const username = "harithabujji";
      const password = "haritha123";
    const hash = Buffer.from(`${username}:${password}`).toString('base64');
    fetch('http://127.0.0.1:8000/onlineapp/clg/', {
   method: 'get',
   headers: new Headers({
     'Authorization': `Basic ${hash}`,
     'Content-Type': 'application/x-www-form-urlencoded',
   }),
 })
     .then(response => response.json())
        .then(responseJson => {
         console.log('responseJson',responseJson);
        this.setState({ collegesList : responseJson});
        })
        .catch(e => {console.log ("Error");});
//        const{name,pass} = this.state;
//        fetch("http://127.0.0.1:8000/onlineapp/clg/",{
//
//            method:'post',
//            headers:{
//                "Content-type":"application/x-www-form-urlencoded; charset=UTF-8"
//            },
//
//            body:'username = ${name}&password=${pass}'
//            }).then(res=>res.json()).then(response=>{
//
//                console.log('response',response);
//            })
        }

        render(){

            return(<div>

                <input onChange = {this.saveName} name = "name"/>
                <br/>
                <input onChange = {this.savePass} name = "pass"/>
                <br/>

                <button onClick={this.submit}>Submit</button>
                </div>)

        }

}

export default InputEx