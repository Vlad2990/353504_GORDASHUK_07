import fetch from "node-fetch";

const CLARIFAI_PAT = "a2f7f2ec82464a09bf671101d2689ab3";
const USER_ID = "clarifai";
const APP_ID = "main";

export const Detect = async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: "Файл обязателен" });
  }

  try {
    const base64Image = req.file.buffer.toString("base64");

    const response = await fetch(
      "https://api.clarifai.com/v2/models/general-image-recognition/outputs",
      {
        method: "POST",
        headers: {
          "Authorization": `Key ${CLARIFAI_PAT}`,
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          user_app_id: {
            user_id: USER_ID,
            app_id: APP_ID
          },
          model_id: "general-detection",
          inputs: [
            { data: { image: { base64: base64Image } } }
          ]
        }),
      }
    );

    const data = await response.json();

    if (data.status.code !== 10000) {
      console.error("Ошибка от Clarifai:", data.status);
      return res.status(500).json({ error: data.status.description });
    }

    const concepts = data.outputs[0].data.concepts.map(c => ({
      name: c.name,
      confidence: c.value
    }));

    res.json({ concepts });

  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Ошибка при распознавании изображения" });
  }
};

