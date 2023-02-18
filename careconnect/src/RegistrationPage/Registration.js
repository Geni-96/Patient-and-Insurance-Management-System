import "./registration.css"


export default function Registration(){
    return(
    <div className="regpage">
        <div className="cover">
            <h2>Registration</h2>
            <form action="form.html"/>
            <input type="text" placeholder="Enter your name" id="name" /><br/>
            <input type="text" placeholder="Enter your email" id="email" /><br/>
            <input type="password" placeholder="Enter your password" id="password" /><br/>
        </div>
    </div>)
}