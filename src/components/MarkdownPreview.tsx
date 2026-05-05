import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import rehypeRaw from "rehype-raw";

export function MarkdownPreview({ source }: { source: string }) {
  return (
    <div className="prose-readme">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        rehypePlugins={[rehypeRaw]}
        components={{
          td: ({ node, ...props }) => {
            const nextProps: Record<string, unknown> = { ...props };
            if ("vAlign" in nextProps) {
              nextProps.valign = nextProps.vAlign as string;
              delete nextProps.vAlign;
            }
            return <td {...nextProps} />;
          },
          th: ({ node, ...props }) => {
            const nextProps: Record<string, unknown> = { ...props };
            if ("vAlign" in nextProps) {
              nextProps.valign = nextProps.vAlign as string;
              delete nextProps.vAlign;
            }
            return <th {...nextProps} />;
          },
        }}
      >
        {source}
      </ReactMarkdown>
    </div>
  );
}
