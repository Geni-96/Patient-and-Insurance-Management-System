import './App.css'

export default function login() {
  return (
    <div id="logo">
      <div id="pane1" className="card">
        <img src={require("./CareConnect.png")} />
      </div>
      <div id="pane2" className="card">
        <div className="box">
          <img src="https://cdn-icons-png.flaticon.com/512/6681/6681204.png" />
          <h2>Login</h2>
        </div>
        <div className="form">
          <form action="form.html"/>
          <div id="radio">
            <label className="usertype">Doctor</label>
            <input type="radio" id="usertype" value="Doctor"/>
            <label className="usertype">Patient</label>
            <input type="radio" id="usertype" value="Patient"/>
            <label className="usertype">InsuranceProvider</label>
            <input type="radio" id="usertype" value="Insurance Provider"/><br/>
          </div>

          
          <input type="text" placeholder="Email/Phone" /><br/> 
          <input type="password" placeholder="Password" id="password"/><br/>
          <input type="submit" id="Login submission" value="Submit"></input>
          <p>Don't have an account? Create an account</p>
        </div>
      </div>
    </div>
  )
}
