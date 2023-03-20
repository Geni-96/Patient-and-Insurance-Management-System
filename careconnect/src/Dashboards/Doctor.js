import React from 'react'
import "./dashboard_styles.css"
import data from "./data"
import Card from "./Card"

export default function Doctor() {
    const cards = data.map(item => {
        return (
            <Card
                key={item.id}
                {...item}
            />
        )
    }) 
  return (
    <main>
        <nav className = "doc-nav">
            <img src={process.env.PUBLIC_URL + "/react-logo.png"} className="logo"></img>
            <div className="search-wrap">
                <select class="dropdown">
                    <option value="Doctor">Doctor</option>
                    <option value="Insurance Provider">Insurance Provider</option>
                </select>
                <div className="search">
                    <input type="text" placeholder="Search"></input>
                    <button type="submit"><i class="fa fa-search"></i></button>
                </div>
            </div>
        </nav>
        <div className="page">
            <div className="page-buttons">
                <button className="buttons-appointment" type="text">UpComing Appointments</button>
                <button className="buttons-appointment" type="text">Past Appointments</button>
            </div>
            <div className="results">
            <section className="cards-list">
                {cards}
            </section>
            </div>
        </div>
    </main>
  )}