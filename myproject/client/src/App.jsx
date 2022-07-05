import { useState } from 'react'
import { Routes, Route } from 'react-router-dom'

import Search from './pages/Search/Search'
import VideoResults from './pages/VideoResults/VideoResults'

function App() {
    const [videos, setVideos] = useState({})

    return (
        <div className="App">
            <Routes>
                <Route path="/" element={<Search setVideos={setVideos} />} />
                <Route
                    path="/videos"
                    element={<VideoResults videos={videos} />}
                />
            </Routes>
        </div>
    )
}

export default App
