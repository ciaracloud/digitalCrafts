import React from "react";

export default function Image(props) {
  const { images } = props;
  console.log(images);
  return (
    <div>
      <img src={images.url} />
    </div>
  );
}
