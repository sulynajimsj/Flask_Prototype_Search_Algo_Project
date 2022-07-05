import React from 'react'
import LoadingSpinner from './LoadingSpinner/LoadingSpinner'

import './VideoResults.css'

export default function VideoResults({ videos }) {
    console.log(videos)

    return (
        <div>
            {Object.keys(videos).length === 0 ? (
                <LoadingSpinner />
            ) : (
                <div className="videos">
                    {videos.map((video, index) => {
                        return (
                            <a href={video.link} key={index}>
                                <div className="single-video">
                                    <div className="thumbnail">
                                        <img
                                            src={video.thumbnail.static}
                                            alt=""
                                        />
                                        <div className="video-length">
                                            {video.length}
                                        </div>
                                    </div>
                                    <div className="video-details">
                                        <div className="title">
                                            {video.title}
                                        </div>
                                        <div className="channel-name">
                                            {video.channel.name}
                                        </div>
                                        <div className="views">
                                            {video.views} views
                                        </div>
                                    </div>
                                </div>
                            </a>
                        )
                    })}
                </div>
            )}
        </div>
    )
}
