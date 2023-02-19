import './login.css'

export default function login() {
  return (
    <div className='loginpage'>
      <div className='cover'>
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
              <label name="usertype">Doctor</label>
              <input type="radio" id="usertype" value="Doctor"/>
              <label name="usertype">Patient</label>
              <input type="radio" id="usertype" value="Patient"/>
              <label name="usertype">InsuranceProvider</label>
              <input type="radio" id="usertype" value="Insurance Provider"/><br/>
            </div>

            
            <input type="text" placeholder="Email" id="email" required/><br/> 
            <input type="password" placeholder="Password" id="password" required/><br/>
            <input type="submit" id="submit" value="Login"></input>
            <p>Don't have an account? Create an account</p>
          </div>
        </div>
      </div>
    </div>
  )
}