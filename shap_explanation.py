def shap_explanation(model, explainer, input_df):
    import plotly.graph_objects as go
    import plotly.io as pio

    shap_values = explainer(input_df)

    shap_vals = shap_values.values
    if len(shap_vals.shape) == 3:
        shap_vals = shap_vals[0, :, 1]
    else:
        shap_vals = shap_vals[0]

    feature_names = input_df.columns

    contributions = list(zip(feature_names, shap_vals))
    contributions.sort(key=lambda x: abs(float(x[1])), reverse=True)

    explanations = []
    for feature, value in contributions[:3]:
        impact = abs(float(value)) * 50
        if value > 0:
            explanations.append(
                f"{feature.replace('_', ' ').title()} increased your chances by {impact:.1f}% ⬆️"
            )
        else:
            explanations.append(
                f"{feature.replace('_', ' ').title()} decreased your chances by {impact:.1f}% ⬇️"
            )

    sorted_pairs = sorted(
        zip(list(feature_names), shap_vals.tolist()),
        key=lambda x: abs(x[1])
    )
    feat_labels = [p[0].replace("_", " ").title() for p in sorted_pairs]
    feat_values = [float(p[1]) for p in sorted_pairs]

    bar_colors   = ["#667eea" if v >= 0 else "#f59e0b" for v in feat_values]
    border_colors = ["#8b9ef5" if v >= 0 else "#fbbf24" for v in feat_values]

    hover_texts = [
        f"<b>{label}</b><br>"
        f"SHAP value: {'+'if v>=0 else ''}{v:.4f}<br>"
        f"{'Positive' if v >= 0 else 'Negative'} impact on shortlisting"
        for label, v in zip(feat_labels, feat_values)
    ]

    bar_labels = [f"{'+'if v>=0 else ''}{v:.3f}" for v in feat_values]

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=feat_values,
        y=feat_labels,
        orientation="h",
        marker=dict(
            color=bar_colors,
            line=dict(color=border_colors, width=1),
            opacity=0.9,
        ),
        text=bar_labels,
        textposition="outside",
        textfont=dict(
            color="rgba(255,255,255,0.7)",
            size=11,
            family="Outfit, Segoe UI, sans-serif",
        ),
        hovertemplate="%{customdata}<extra></extra>",
        customdata=hover_texts,
        cliponaxis=False,
    ))

    fig.add_vline(
        x=0,
        line=dict(color="rgba(255,255,255,0.2)", width=1.2, dash="solid"),
        layer="below"
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#0e0820",

        font=dict(
            family="Outfit, Segoe UI, sans-serif",
            color="#ffffff",
        ),

        title=dict(
            text="<b>Feature Impact on Your Result</b>",
            font=dict(size=18, color="#ffffff", family="Syne, Segoe UI, sans-serif"),
            x=0,
            xanchor="left",
            pad=dict(b=16),
        ),

        xaxis=dict(
            title=dict(
                text="SHAP Value (Impact on prediction)",
                font=dict(size=14, color="rgba(255,255,255,0.69)"),
            ),
            tickfont=dict(size=10, color="rgba(255,255,255,0.48)"),
            gridcolor="rgba(255,255,255,0.22)",
            gridwidth=1,
            zeroline=False,
            showline=False,
            tickformat=".3f",
        ),

        yaxis=dict(
            tickfont=dict(size=13, color="#ffffff"),
            gridcolor="rgba(0,0,0,0)",
            showgrid=False,
            showline=False,
            automargin=True,
        ),

        margin=dict(l=10, r=60, t=48, b=40),

        hoverlabel=dict(
            bgcolor="#1a0f35",
            bordercolor="rgba(102,126,234,0.4)",
            font=dict(
                size=12,
                color="#ffffff",
                family="Outfit, Segoe UI, sans-serif",
            ),
        ),

        bargap=0.35,
        height=500,
    )

    plot_html = pio.to_html(
        fig,
        full_html=False,
        include_plotlyjs="cdn",
        config={
            "displaylogo": False,
            "modeBarButtonsToRemove": [
                "zoom2d", "pan2d", "select2d", "lasso2d",
                "zoomIn2d", "zoomOut2d", "autoScale2d",
                "hoverCompareCartesian", "hoverClosestCartesian",
                "toggleSpikelines",
            ],
            "responsive": True,
        },
    )

    return explanations, plot_html