import { useState, useEffect } from 'react'
import { Link, Outlet, Routes, Route } from 'react-router-dom'

import { rightArrow } from '../../SVGs/SVG'

import './Search.css'

export default function Search({ setVideos }) {
    const [URL, setURL] = useState('')
    const [image, setImage] = useState('')
    const [submitted, setSubmitted] = useState(false)

    function clickHandler() {
        fetch('/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                text: image,
            }),
        })
            .then((res) => res.json())
            .then((data) => {
                setVideos(() => {
                    return data['video_results']
                })
                // console.log(data['video_results'])
            })
    }

    return (
        <div className="Search">
            <form
                action=""
                onSubmit={(e) => {
                    e.preventDefault()
                    console.log('submitted')
                    setImage(() => {
                        return URL
                    })
                    setSubmitted(() => {
                        return true
                    })
                }}
            >
                <div className="url-search">
                    <input
                        type="text"
                        className="url-input"
                        value={URL}
                        placeholder="Enter a URL"
                        onChange={(e) => {
                            setURL(() => {
                                return e.target.value
                            })
                        }}
                    />
                </div>
                {submitted && (
                    <div className="searched-img-container">
                        <img className="searched-img" src={image} alt="URL" />
                        <Link to="/videos">
                            <div className="right-arrow" onClick={clickHandler}>
                                {rightArrow}
                            </div>
                        </Link>
                    </div>
                )}
            </form>
        </div>
    )
}
